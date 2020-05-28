def dsrp_family(who='Father',name='Kidd'):
    """描述家庭成员的组成信息"""
    print("\nThere is " + who.lower() + " in the family." )
    print(name.title() + "!")

dsrp_family()
dsrp_family('Mother','Belle')
dsrp_family(who='Baby',name='Harry')
dsrp_family(name='Zhenqing',who='Baby')

def getFormalName(first_name,last_name,middle_name=''):
    """Return formal name"""
    if middle_name:
        full_name = first_name + '*' + middle_name + '*' + last_name
    else:
        full_name = first_name + '*' + last_name
    return full_name

harry_fullname = getFormalName('Harry','Young')
print(harry_fullname)

print(getFormalName('Kidd','Young'))

def build_person(first_name,last_name,age=''):
    """Return a dict"""
    person = {'first':first_name,'last':last_name}
    if age:
        person['age'] = age
    return person

print(build_person('Harry','Young',1))
