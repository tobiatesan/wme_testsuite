import struct

headers = {
    1: 40,
    2: 52,
    3: 56,
    4: 108,
    5: 124,
}

for i, comp, fname, oname in [
    (5, 3, "a32bit5.bmp", "v5a32bit.bmp"),
    (4, 3, "a32bit4.bmp", "v4a32bit.bmp"),
    (3, 0, "a32bit3.bmp", "v3a32bit.bmp"),
    (2, 0, "a32bit2.bmp", "v2a32bit.bmp"),
    (1, 0, "a32bit1.bmp", "v1a32bit.bmp"),

    (5, 0, "ck32bit5.bmp", "v5ck32bit.bmp"),
    (4, 0, "ck32bit4.bmp", "v4ck32bit.bmp"),
    (3, 0, "ck32bit3.bmp", "v3ck32bit.bmp"),
    (2, 0, "ck32bit2.bmp", "v2ck32bit.bmp"),
    (1, 0, "ck32bit1.bmp", "v1ck32bit.bmp"),

    (5, 0, "ck24bit5.bmp", "v5ck24bit.bmp"),
    (4, 0, "ck24bit4.bmp", "v4ck24bit.bmp"),
    (3, 0, "ck24bit3.bmp", "v3ck24bit.bmp"),
    (2, 0, "ck24bit2.bmp", "v2ck24bit.bmp"),
    (1, 0, "ck24bit1.bmp", "v1ck24bit.bmp"),

    (5, 1, "ck8bit5.bmp", "v5ck8bit.bmp"),
    (4, 1, "ck8bit4.bmp", "v4ck8bit.bmp"),
    (3, 1, "ck8bit3.bmp", "v3ck8bit.bmp"),
    (2, 1, "ck8bit2.bmp", "v2ck8bit.bmp"),
    (1, 1, "ck8bit1.bmp", "v1ck8bit.bmp"),

    (5, 0, "ck4bit5.bmp", "v5ck4bit.bmp"),
    (4, 0, "ck4bit4.bmp", "v4ck4bit.bmp"),
    (3, 0, "ck4bit3.bmp", "v3ck4bit.bmp"),
    (2, 0, "ck4bit2.bmp", "v2ck4bit.bmp"),
    (1, 0, "ck4bit1.bmp", "v1ck4bit.bmp"),
]:
    with open(fname, "rb") as f:
        data = bytearray(f.read())
    
    header_data = struct.unpack('<2sIHHIIIIHHIIIIII', data[:54])
    bm, fsize, r1, r2, offset, hsize, w, h, pl, bpp, i1, i2, i3, i4, i5, i6 = header_data
    if hsize < headers[i]:
        raise(Exception(hsize, i, fname))

    image_data = data[14 + hsize:]

    other_data = data[54:14 + headers[i]]
    
    i1 = comp
    fsize = fsize - hsize + headers[i]
    offset = offset - hsize + headers[i]
    hsize = headers[i]
    header_data = struct.pack('<2sIHHIIIIHHIIIIII', bm, fsize, r1, r2, offset, hsize, w, h, pl, bpp, i1, i2, i3, i4, i5, i6)

    with open(oname, "wb") as f:
        f.write(header_data)
        f.write(other_data)
        f.write(image_data)
