from openpyxl import load_workbook
import database

def Excel():
    wb = load_workbook('SampleData.xlsx')

    # 현재 Active Sheet 얻기
    ws = wb.active
    pre = ws.rows

    for r in ws.rows:  # 엑셀에서 각 행과 열로 순회하기 위함
        OrderDate = r[0].value  # 첫째 열의 값 : 그룹
        data = r[2].value  # 둘째 열의 값 : 주소

        print(OrderDate)
        print(data)
        database.insert(OrderDate, data, data)
        # print(r)


if __name__ == "__main__":
    Excel()
