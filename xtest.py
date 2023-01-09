import time

if __name__ == '__main__':
    start_time = time.time()
    for i in range(0,16000000000000):
        pass
    print("--- %s seconds ---" % (time.time() - start_time))