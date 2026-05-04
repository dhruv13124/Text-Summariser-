import os 
from textsummarizer.logging import logger
from transformers import AutoTokenizer
from datasets import load_dataset, load_from_disk 
from textsummarizer.entity import DataIngestionConfig




class DataTransformation:
    def __init__(self, config):
        self.config = config
        self.tokenizer = AutoTokenizer.from_pretrained(config.tokenizer_name)

    def convert_examples_to_features(self, example_batch):
        model_inputs = self.tokenizer(
            example_batch["dialogue"],
            max_length=1024,
            truncation=True,
            padding="max_length"
        )

        labels = self.tokenizer(
            text_target=example_batch["summary"],
            max_length=128,
            truncation=True,
            padding="max_length"
        )

        labels_ids = [
            [(t if t != self.tokenizer.pad_token_id else -100) for t in label]
            for label in labels["input_ids"]
        ]

        model_inputs["labels"] = labels_ids
        return model_inputs

    def convert(self):  
        dataset_samsum = load_from_disk(self.config.data_path)

        dataset_samsum_pt = dataset_samsum.map(
            self.convert_examples_to_features,
            batched=True
        )

        dataset_samsum_pt.save_to_disk(
            os.path.join(self.config.root_dir, "samsum_dataset")
        )