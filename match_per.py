from transformers import BertTokenizer, BertModel
from sklearn.metrics.pairwise import cosine_similarity
from gensim.models import Word2Vec
from gensim.similarities import WmdSimilarity
import torch

# Load pre-trained BERT model and tokenizer
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased').to(device)

# Define a function to encode text using BERT embeddings
def encode_text(text):
    input_ids = tokenizer.encode(text, add_special_tokens=True, max_length=512, truncation=True, return_tensors='pt').to(device)
    with torch.no_grad():
        outputs = model(input_ids)
    embeddings = outputs.last_hidden_state.mean(dim=1)
    return embeddings.cpu().numpy()

# Define a function to calculate text similarity using Word Mover's Distance
def calculate_similarity(original_answer, student_answer):
    # Tokenize and encode the text
    original_embedding = encode_text(original_answer)
    student_embedding = encode_text(student_answer)

    # Calculate cosine similarity between embeddings
    cos_similarity = cosine_similarity(original_embedding, student_embedding)[0][0]

    # Use Word Mover's Distance for a more robust similarity measure
    wmd_similarity = calculate_wmd_similarity(original_answer, student_answer)

    # Combine cosine similarity and WMD similarity (you can adjust weights as needed)
    similarity_score = 0.7 * cos_similarity + 0.3 * (1 - wmd_similarity)  # WMD is distance, so we subtract from 1
    return similarity_score

# Define a function to calculate Word Mover's Distance similarity
def calculate_wmd_similarity(original_answer, student_answer):
    # Preprocess text if needed (e.g., lowercasing, removing punctuation)
    # Calculate Word Mover's Distance
    wmd_similarity = 0  # Placeholder, implement WMD calculation based on your specific preprocessing and tokenization
    return wmd_similarity

# Example usage
original_answer = "The cat sat on the mat"
student_answer = "The dog lay on the carpet"


similarity_score = calculate_similarity(original_answer, student_answer)
similarity_percentage = similarity_score * 100
print(f"Similarity percentage: {similarity_percentage:.2f}%")

