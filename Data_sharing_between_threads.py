from threading import Thread
from pydantic import BaseModel  # 構造体に型強制させることで型安全にできる
from time import sleep


# インスタンスの参照で変数にアクセスするためのクラス
class GlobalVariable(BaseModel):
    count: int = 0

    # 再代入時にも型検証を実施
    class Config:
        validate_assignment = True


def func_1(global_memory: GlobalVariable):
    for _ in range(100):
        global_memory.count += 1
        print(global_memory.count)
        sleep(0.1)


def func_2(global_memory: GlobalVariable):
    for _ in range(100):
        global_memory.count -= 1
        sleep(0.1)


# インスタンス化
global_memory = GlobalVariable()

# インスタンスの参照をargsに与える
thread1 = Thread(target=func_1, args=[global_memory])
thread2 = Thread(target=func_2, args=[global_memory])

thread1.start()
thread2.start()

thread1.join()

print("all work completed")
