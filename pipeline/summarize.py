def split_chunks(text, chunk_size = 3000):
    chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]
    return chunks