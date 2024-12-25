import pandas as pd


class Clean:
    @classmethod
    def clean(
        self,
        data: pd.DataFrame 
    ) -> pd.DataFrame:
        assert type(data) == pd.DataFrame, f"The input must be pd.DataFrame, not {type(data)}"

        # fill na
        for column in data.columns:
            data[column].fillna(method="bfill", inplace=True)
            data[column].fillna(method="ffill", inplace=True)

            # in case there is only one row
            if data[column].dtype == "object":
                data[column].fillna(value="0", inplace=True)
            elif data[column].dtype == "float":
                data[column].fillna(value=0.0, inplace=True)

        # one hot encoder
        for column in data.columns:
            if data[column].dtype == "object":
                print(list(data[column].unique()))
                print([i for i in range(len(list(data[column].unique())))])
                data[column].replace(list(data[column].unique()), [i for i in range(len(data[column].unique()))], inplace=True)

        # drop id
        data.drop("ID", axis=1, inplace=True)

        return data