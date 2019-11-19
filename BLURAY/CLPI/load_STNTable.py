def load_STNTable(fobj, length2, length2a):
    # NOTE: see https://github.com/lerks/BluRay/wiki/STNTable

    # Import modules ...
    import struct

    # Load sub-functions ...
    from .load_StreamAttributes import load_StreamAttributes
    from .load_StreamEntry import load_StreamEntry

    # Initialize variables ...
    ans = {}
    length2b = 0                                                                                                        # [B]

    # Read the binary data ...
    ans["Length"], = struct.unpack(">H", fobj.read(2));                                                                 length2 += 2; length2a += 2
    fobj.read(2);                                                                                                       length2 += 2; length2a += 2; length2b += 2
    ans["NumberOfPrimaryVideoStreamEntries"], = struct.unpack(">B", fobj.read(1));                                      length2 += 1; length2a += 1; length2b += 1
    ans["NumberOfPrimaryAudioStreamEntries"], = struct.unpack(">B", fobj.read(1));                                      length2 += 1; length2a += 1; length2b += 1
    ans["NumberOfPrimaryPGStreamEntries"], = struct.unpack(">B", fobj.read(1));                                         length2 += 1; length2a += 1; length2b += 1
    ans["NumberOfPrimaryIGStreamEntries"], = struct.unpack(">B", fobj.read(1));                                         length2 += 1; length2a += 1; length2b += 1
    ans["NumberOfSecondaryAudioStreamEntries"], = struct.unpack(">B", fobj.read(1));                                    length2 += 1; length2a += 1; length2b += 1
    ans["NumberOfSecondaryVideoStreamEntries"], = struct.unpack(">B", fobj.read(1));                                    length2 += 1; length2a += 1; length2b += 1
    ans["NumberOfSecondaryPGStreamEntries"], = struct.unpack(">B", fobj.read(1));                                       length2 += 1; length2a += 1; length2b += 1
    fobj.read(5);                                                                                                       length2 += 5; length2a += 5; length2b += 5

    # Loop over stream list names ...
    for name in ["PrimaryVideoStreamEntries", "PrimaryAudioStreamEntries", "PrimaryPGStreamEntries", "SecondaryPGStreamEntries", "PrimaryIGStreamEntries", "SecondaryAudioStreamEntries", "SecondaryVideoStreamEntries"]:
        # Loop over entries and add to list ...
        ans[name] = []
        # print("\t\t", name, " starts: ", fobj.tell() * 8, "剩余长度：", (7578 - fobj.tell()) * 8)
        for i in range(ans["NumberOf{0:s}".format(name)]):
            tmp = {}
            # print("\t\t\t " + str(i) + " load_StreamEntry starts at: ", fobj.tell() * 8, "剩余长度：", (7578 - fobj.tell()) * 8)
            res, length2, length2a, length2b, length2c = load_StreamEntry(fobj, length2, length2a, length2b)
            tmp["StreamEntry"] = res
            # print("\t\t\tload_StreamAttributes starts at: ", fobj.tell() * 8, "剩余长度：", (7578 - fobj.tell()) * 8)
            res, length2, length2a, length2b, length2c = load_StreamAttributes(fobj, length2, length2a, length2b)
            tmp["StreamAttributes"] = res
            ans[name].append(tmp)
            # print("\t\t\tload_StreamAttributes ends at: ", fobj.tell() * 8, "剩余长度：", (7578 - fobj.tell()) * 8)

    # Pad out the read ...
    if length2b != ans["Length"]:
        l = ans["Length"] - length2b                                                                                    # [B]
        fobj.read(l);                                                                                                   length2 += l; length2a += l; length2b += l

    # Return answer ...
    return ans, length2, length2a, length2b
