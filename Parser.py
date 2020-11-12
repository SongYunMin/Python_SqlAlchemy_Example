from openpyxl import load_workbook
import database


def Excel():
    wb = load_workbook('SampleData.xlsx')

    # 현재 Active Sheet 얻기
    ws = wb.active
    pre = ws.rows

    for r in ws.rows:  # 엑셀에서 각 행과 열로 순회하기 위함
        OrderDate = r[0].value  # 첫째 열의 값 : 그룹
        Region = r[1].value
        Rep = r[2].value
        Item = r[3].value  # 둘째 열의 값 : 주소
        Units = r[4].value
        Unit_Cost = r[5].value
        East_Regula = r[6].value
        Total = r[7].value
        print(OrderDate)
        database.insert(OrderDate, Region, Rep, Item, Units, Unit_Cost, East_Regula, Total)



if __name__ == "__main__":
    Excel()
