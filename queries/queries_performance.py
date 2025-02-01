import time
from case_insesitive_search import search_case_insensitive_single_word, search_case_insensitive_multiple_words
from case_sensitive_search import search_case_sensitive_single_word, search_case_sensitive_multiple_words
from fuzzy_search import search_fuzzy
from aggregation_search import aggregate_by_category, aggregate_title_length
from multiple_fields_search import search_multiple_fields, search_by_date
from multiple_terms_search import search_terms, search_wildcard

# start_time = time.time()
# search_case_insensitive_single_word("Effective Recommendations")
# print(f"Execution time: {time.time() - start_time} seconds")

# start_time = time.time()
# search_case_insensitive_multiple_words(["Effective Recommendations"])
# print(f"Execution time: {time.time() - start_time} seconds")

# start_time = time.time()
# search_case_sensitive_single_word("AUDIO DATA")
# print(f"Execution time: {time.time() - start_time} seconds")

# start_time = time.time()
# search_case_sensitive_multiple_words(["Effective Recommendations"])
# print(f"Execution time: {time.time() - start_time} seconds")

# start_time = time.time()
# search_fuzzy("nerual network")
# print(f"Execution time: {time.time() - start_time} seconds")

# start_time = time.time()
# print(aggregate_by_category())
# print(f"Execution time: {time.time() - start_time} seconds")

# start_time = time.time()
# search_multiple_fields("Deep Learning Pipeline described")
# print(f"Execution time: {time.time() - start_time} seconds")

# start_time = time.time()
# search_terms(["deep learning"], ["AI", "neural networks"], ["statistics"])
# print(f"Execution time: {time.time() - start_time} seconds")

# start_time = time.time()
# search_wildcard("deep*learning")
# print(f"Execution time: {time.time() - start_time} seconds")

# start_time = time.time()
# search_by_date()
# print(f"Execution time: {time.time() - start_time} seconds")

# start_time = time.time()
# aggregate_title_length()
# print(f"Execution time: {time.time() - start_time} seconds")