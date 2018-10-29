def my_hash_0(s):
    int_vals = [ord(c) for c in s]
    return sum(int_vals)

def my_hash_1(s):
    int_vals = [2**ord(c) for c in s]
    return sum(int_vals)

def my_hash_2(s):
    int_vals = [2**ord(c) for c in s]
    int_vals = [c**i for i, c in zip(range(1, len(int_vals)+1), int_vals)]
    return sum(int_vals)

def time_hash(hash_fun, uuids):
    hs = [hash_fun(uuid) for uuid in uuids]
    collision_rate = (len(hs) - len(set(hs))) / len(hs)
    collision_rate = round(collision_rate * 100, 2)
    return collision_rate


if __name__ == '__main__':

    with open("./uuid_test.txt", 'r') as f:
        uuid_test = f.readlines()

    with open("./uuid.txt", 'r') as f:
        uuid_full = f.readlines()

    print("Hash 0 collision rate: {}"
           .format(time_hash(my_hash_0, uuid_full)))

    print("Hash 1 collision rate: {}"
           .format(time_hash(my_hash_1, uuid_full)))

    print("Hash 2 collision rate: {}"
       .format(time_hash(my_hash_2, uuid_full)))

    print("Python hash collision rate: {}"
        .format(time_hash(hash, uuid_full)))
