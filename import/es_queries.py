queries = [
  {
      "query": {
          "bool": {
              "must": [
                  {
                      "multi_match": {
                          "query": "Challenge tax word morning over important election",
                          "fields": ["title", "abstract", "content"],
                          "fuzziness": "AUTO",
                          "operator": "and"
                      }
                  }
              ]
          }
      }
  },

  {
      "query": {
          "range": {
              "update_date": {
                  "gte": "2023-01-01",
                  "lte": "2023-06-30"
              }
          }
      },
      "sort": [
          {"update_date": "asc"}
      ]
  },

  {
      "size": 0,
      "query": {
          "bool": {
              "filter": [
                  { "term": { "category.keyword": "cs.LG" } }
              ]
          }
      },
      "aggs": {
          "avg_length": {
              "avg": {
                  "field": "word_count"
              }
          }
      }
  },

  {
      "query": {
          "bool": {
              "should": [
                  {"match_phrase": {"abstract": "computer science"}},
                  {"match": {"category": "cs.AI"}}
              ]
          }
      },
      "sort": [
          {"update_date": "desc"}
      ]
  },

  {
      "query": {
          "bool": {
              "must": [
                  {"match": {"abstract": "full"}},
                  {"match_phrase": {"content": "old task"}}
              ],
              "should": [
                  {"match": {"keywords": "AI"}},
                  {"match": {"keywords": "optimization"}}
              ],
              "must_not": [
                  {"match": {"category": "physics.optics"}}
              ]
          }
      }
  }
]