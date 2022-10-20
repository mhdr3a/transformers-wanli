## Model Evaluation using [WANLI Test Set](https://alisawuffles.github.io/publication/wanli/)

Here is an example of evaluating a model (fine-tuned either on MNLI or SNLI) using WANLI test set [Liu et al., 2022](https://arxiv.org/abs/2201.05955).

The WANLI dataset can be accessed either from [Google Drive](https://drive.google.com/drive/u/0/folders/1tbLcQUF2W9ClanTLv9EWAEFuMz8iQ2AE) or [HuggingFace](https://huggingface.co/datasets/alisawuffles/WANLI).
You may then convert test.jsonl to test.txt (tab separated) using the following Python script:

```python
import csv
import json
with open('data/WANLI/test.jsonl') as old, open('data/WANLI/test.txt', 'w') as csvfile:
  new = csv.writer(csvfile, delimiter='\t')
  first = True
  for x in old:
    row = json.loads(x)
    if first:
      new.writerow(row.keys())
      first = False
    new.writerow(row.values())
```
Next, in test.txt, join the line 4871 to the end of the line 4870 to prevent later errors. If you are working with train.jsonl, you should join the line 3175 to the end of the line 3174 and the line 3204 to that of the line 3203 in train.txt.

This is an example of using run_wanli_mnli.py in Google Colab:

```bash
!git clone https://github.com/mhdr3a/transformers-wanli
!mv /content/transformers-wanli/* /content/
!rm transformers-wanli -r
!pip install -r requirements.txt

!python run_wanli_mnli.py \
        --task_name wanli \
        --do_eval \
        --data_dir data/WANLI \
        --model_name_or_path mnli-6 \
        --max_seq_length 128 \
        --output_dir mnli-6
```
* Note that the mnli-6 model is fine-tuned on MNLI; so, use run_wanli_snli.py if your model is fine-tuned on SNLI.

This will create the wanli_predictions.txt file in ./mnli-6, which can then be evaluated using evaluate_predictions.py.

```bash
!python evaluate_predictions.py ./mnli-6/wanli_predictions.txt
```

The evaluation results for the [mnli-6 model](https://huggingface.co/mahdiyar/mnli-6) is as follows:

```bash
entailment: 0.8456413103831205
neutral: 0.3688736027515047
contradiction: 0.7285318559556787

Overall WANLI Test Evaluation Accuracy: 0.5995050525881626
```

And here are the evaluation results for the [snli-6 model](https://huggingface.co/mahdiyar/snli-6):

```bash
entailment: 0.8278734036646308
neutral: 0.2472055030094583
contradiction: 0.6551246537396122

Overall WANLI Test Evaluation Accuracy: 0.5236131161064137
```
