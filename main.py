email=input(" Enter A Valid Email Address : ")
k,j,d=0,0,0
# at least you have minimun 6 characters in an valid email address 
# using len function we can determine a length of email
if len(email)>=6:
# a valid email address should be start with a alphabet 
  if email[0].isalpha():
# a valid email includes only one "@".
    if ("@"in email) and (email.count("@")==1):
# a valid email has a right position of ".".
      if (email[-4]==".")^(email[-3]=="."):
# checking whether there is a space in email or not 
        for i in email:
          if i==i.isspace():
            k=1 
# now checking whether there is a alphabet in an email 
          elif i.isalpha():
# if the email consists alphabet then checking that email is uppercase or not ..
# if the alphabet in email is uppercase then its a WRONG EMAIL .
            if i==i.upper():
              j=1 
# if the email consists a digit then continue the loop 
          elif i.isdigit():
            continue
# email only consists these three special characters .
          elif i=="_" or i=="." or i=="@":
            continue 
# if an email consists other specail characters then it is a WRONG EMAIL .
          else:
            d=1
        if k==1 or j==1 or d==1:
          print("Wrong Email Address :::: a valid email has no spaces included.")
      else:
        print("Wrong Email Address :::: the position of . is wrong")

    else:
      print("Wrong Email Address :::: a valid email should have a one "@"in it.")
  else:
    print("Wrong Email Address :::: a valid email should be start with a alphabetical letter not a digit, special charcter or space")
else: 
  print("Wrong Email Address :::: At least you have minimun 6 characters using this format -->> a@a.in")
