def Ticket_Pricing(n: int) -> int:
   if n<=5:
      return 0
   elif 6<=n and n<=17:
      return 10
   elif 18<=n and n<=64:
      return 20
   elif n>=65:
      return 15
   pass


if __name__ == '__main__':
    n = int(input())
    print(Ticket_Pricing(n))
