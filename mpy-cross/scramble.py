from ubinascii import crc32


def scramble(payload):
    def scramble_encode(payload):
        def messItUp(v, index, len):
            a = (32 * len * index + 0x7f) & 0xff
            b = index % 8
            c = (1 << b) & 0xff
            d = (c + a) & 0xff
            return (v ^ d) & 0xff

        raw = 0
        for i in range(4):
            raw >>= 8
            byte = payload & 0xff
            payload >>= 8
            new_byte = messItUp(byte, i, 4)
            raw += new_byte << 24
        return raw
    crc = crc32(payload)
    return scramble_encode(crc)


