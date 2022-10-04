from fast_gzip.gzip import RawGzip

f = open("example_data/big.fq.gz", "rb")
r = RawGzip(f)
print(len(r.read_chunk()))
print(len(r.read_chunk()))
