import csv
def csv_reader_generator(csvfile):
    with open(csvfile,"r") as f:
        data=csv.DictReader(f)
        for row in data:
            yield[
                {"name":row["name"]},
                {"email":row["email"]},
                {"age":row["age"]}
            ]
if __name__ =='__main__':
    for row in csv_reader_generator("user_data.csv"):
          print(row)