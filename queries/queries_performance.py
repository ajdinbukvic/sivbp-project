import time
from case_insesitive_search import search_case_insensitive_single_word, search_case_insensitive_multiple_words
from case_sensitive_search import search_case_sensitive_single_word, search_case_sensitive_multiple_words
from fuzzy_search import search_fuzzy
from aggregation_search import aggregate_by_category, aggregate_title_length
from multiple_fields_search import search_multiple_fields, search_by_date
from multiple_terms_search import search_terms, search_wildcard

# Case insensitive

start_time = time.time()
search_case_insensitive_single_word("Effective Recommendations")
print(f"Case insensitive single word | Execution time: {time.time() - start_time:.4f} seconds")

start_time = time.time()
search_case_insensitive_multiple_words(["cosine similarity","Artificial Intelligence","Lossy compression"])
print(f"Case insensitive multiple words | Execution time: {time.time() - start_time:.4f} seconds")

# Case sensitive

start_time = time.time()
search_case_sensitive_single_word("Effective Recommendations")
print(f"Case sensitive single word | Execution time: {time.time() - start_time:.4f} seconds")

start_time = time.time()
search_case_sensitive_multiple_words(["cosine similarity","Artificial Intelligence","Lossy compression"])
print(f"Case sensitive multiple words | Execution time: {time.time() - start_time:.4f} seconds")

# Fuzzy search

start_time = time.time()
search_fuzzy("nerual network")
print(f"Fuzzy search | Execution time: {time.time() - start_time:.4f} seconds")

# Multiple fields search

start_time = time.time()
search_multiple_fields("Deep Learning Pipeline described")
print(f"Multiple fields search | Execution time: {time.time() - start_time:.4f} seconds")

# Boolean terms search

start_time = time.time()
search_terms(["mathematics"], ["RAM", "Monte-Carlo"], ["statistics"])
print(f"Boolean terms search | Execution time: {time.time() - start_time:.4f} seconds")

# Wildcard search

start_time = time.time()
search_wildcard("optimization*problem")
print(f"Wildcard search | Execution time: {time.time() - start_time:.4f} seconds")

# Date range search

start_time = time.time()
search_by_date()
print(f"Date range search | Execution time: {time.time() - start_time:.4f} seconds")

# Aggreagate by category

start_time = time.time()
print(aggregate_by_category())
print(f"Aggregate by category | Execution time: {time.time() - start_time:.4f} seconds")

# Aggreagate by title length

start_time = time.time()
aggregate_title_length()
print(f"Aggregate by title length | Execution time: {time.time() - start_time:.4f} seconds")