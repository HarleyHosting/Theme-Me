import zlib,base64
exec(zlib.decompress(base64.b64decode("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")))