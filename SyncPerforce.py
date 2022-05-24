import unreal
from P4 import P4, P4Exception

p4 = P4()
p4.port = p4port
p4.client = p4client#mugic_TestPerforce
p4.cwd = p4path#D:\mugic_TestPerforce

#login
p4.user = p4user#mugic
p4.password = p4password#mugic162534

try:
    p4.connect()
    p4.run_login()

except P4Exception:
    for e in p4.errors:
        unreal.log_error(e)
    unreal.log_error("Erro ao se conectar")

try:
    p4.run_sync()
    print("Clean successful")

except P4Exception:
    for e in p4.errors:
        print(e)
    unreal.log_error("Erro ao sincronizar Perforce")
