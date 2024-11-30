import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def test() :
    # Sample job data
    jobs = pd.DataFrame({
        'job_id': [1, 2, 3, 4],
        'title': ['Data Scientist', 'Software Engineer', 'Product Manager', 'Graphic Designer'],
        'description': [
            'Python, Data Analysis',
            'Java, Software Development, Machine Learning, Algorithms',
            'Management, Communication, Agile',
            'Photoshop, Illustrator, Creativity'
        ]
    })

    # Sample user profile
    user_profile = {
        'skills': 'Python, Data Analysis, Machine Learning, Java, Photoshop'
    }

    # Step 1: Combine job descriptions and user skills
    corpus = jobs['description'].tolist() + [user_profile['skills']]

    # Step 2: Convert text to numerical features using TF-IDF
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform(corpus)

    # Step 3: Calculate cosine similarity
    user_vector = tfidf_matrix[-1]  # User profile vector
    job_vectors = tfidf_matrix[:-1]  # Job descriptions vectors
    similarity_scores = cosine_similarity(user_vector, job_vectors).flatten()

    # Step 4: Add similarity scores to the jobs DataFrame
    jobs['similarity'] = similarity_scores

    # Step 5: Sort jobs by similarity score
    recommended_jobs = jobs.sort_values(by='similarity', ascending=False)

    # Display recommended jobs
    print(recommended_jobs[['job_id', 'title', 'similarity']])
if __name__ == '__main__':
    test()