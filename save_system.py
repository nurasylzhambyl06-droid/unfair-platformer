import json

class SaveSystem:

    FILE="save.json"

    @staticmethod
    def save(best):

        try:

            with open(
                SaveSystem.FILE,
                "w"
            ) as f:

                json.dump(
                    {"best":best},
                    f
                )

        except:
            print("save error")

    @staticmethod
    def load():

        try:

            with open(
                SaveSystem.FILE,
                "r"
            ) as f:

                data=json.load(f)

                return data["best"]

        except:

            return 999