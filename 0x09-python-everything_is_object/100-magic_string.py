#!/usr/bin/python3
def magic_string(magic=[0]):
    magic[0] = magic[0] + 1
    return (("BestSchool".join(" ,") * magic[0])[:-1])
