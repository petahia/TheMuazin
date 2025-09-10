import base64


def decode_hostile_lists(encode_string1,encode_string2):
    base64_string1 = encode_string1
    base64_string2 = encode_string2

    decoded_bytes1 = base64.b64decode(base64_string1)
    decoded_bytes2 = base64.b64decode(base64_string2)

    decoded_string1 = decoded_bytes1.decode('utf-8')
    decoded_string2 = decoded_bytes2.decode('utf-8')

    return decoded_string1.split(","),decoded_string2.split(",")


hostile_lists = 'R2Vub2NpZGUsV2FyIENyaW1lcyxBcGFydGhlaWQsTWFzc2FjcmUsTmFrYmEsRGlzcGxhY2VtZW50LEh1bWFuaXRhcmlhbiBDcmlzaXMsQmxvY2thZGUsT2NjdXBhdGlvbixSZWZ1Z2VlcyxJQ0MsQkRT'
non_hostile_lists = 'RnJlZWRvbSBGbG90aWxsYSxSZXNpc3RhbmNlLExpYmVyYXRpb24sRnJlZSBQYWxlc3RpbmUsR2F6YSxDZWFzZWZpcmUsUHJvdGVzdCxVTlJXQQ=='



for i,list in enumerate(decode_hostile_lists(hostile_lists,non_hostile_lists)):
    print(f"{i}.{list}")

