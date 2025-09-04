## Instructions
1. First clone library called lighteval

## Task 1.
2. Implement a feature that updates the markdown results table to display (reported after all tasks are evaluated in CLI), for each task, with the number of samples that were run.
Current behavior
```
|                 Task                  |Version|Metric|Value |   |Stderr|
|---------------------------------------|-------|------|-----:|---|------|
|all                                    |       |chrf++|0.2059|   |      |
|                                       |       |bleu  |0.0000|   |      |
|                                       |       |bleu_1|0.0000|   |      |
|                                       |       |bleu_4|0.0000|   |      |
|lighteval:flores200:eng_Latn-fra_Latn:0|       |chrf++|0.2059|   |      |
|                                       |       |bleu  |0.0000|   |      |
|                                       |       |bleu_1|0.0000|   |      |
|                                       |       |bleu_4|0.0000|   |      |
```

Expected behavior
```
|                 Task                  |Version|Metric|Value |   |Stderr|Samples
|---------------------------------------|-------|------|-----:|---|------|------
|all                                    |       |chrf++|0.2059|   |      |1
|                                       |       |bleu  |0.0000|   |      |
|                                       |       |bleu_1|0.0000|   |      |
|                                       |       |bleu_4|0.0000|   |      |
|lighteval:flores200:eng_Latn-fra_Latn:0|       |chrf++|0.2059|   |      |1
|                                       |       |bleu  |0.0000|   |      |
|                                       |       |bleu_1|0.0000|   |      |
|                                       |       |bleu_4|0.0000|   |      |
```

3. To test your implementation you can use following command:
```
lighteval accelerate --custom-tasks "lighteval.tasks.multilingual.tasks" --max-samples=1 "model_name=openai-community/gpt2,max_length=10" "lighteval|flores200:eng_Latn-fra_Latn|0|0"
```

## Task 2.
2. Then create a new metric called Commet, remove all current metrics in flores200 and add only yourly newly implemented commet metric. The flores definition can be found in `lighteval/src/lighteval/tasks/multilingual/tasks.py`
3. For commet metric you should use the `Unbabel/XCOMET-XL` and report the system score `system_score`
4. Finally you can test your implementation by running (you must use datasetes==3.0.0):

```
lighteval accelerate --custom-tasks "lighteval.tasks.multilingual.tasks" --max-samples=1 "model_name=openai-community/gpt2,max_length=10" "lighteval|flores200:eng_Latn-fra_Latn|0|0"
```