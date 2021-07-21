# def compare(s):
#     for letter in s:
#         if s.count(letter) > 1:
#             print("Not Unique")
#             return
#     print("All Unique")    

# compare("Markiplier")

def getUniqueCharacter(s):

    s = set(s)
 
    return len(s)

if __name__ == "__main__":
    s = "hackthesystem"
 
    print(getUniqueCharacter(s))