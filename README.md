# 🎵 Spotify Hit Song Predictor (Machine Learning Web App)

<p align="center">
  <img src="https://img.shields.io/badge/ML-Project-blue" />
  <img src="https://img.shields.io/badge/Streamlit-Deployed-brightgreen" />
  <img src="https://img.shields.io/badge/Accuracy-99%25-orange" />
</p>

## 🚀 Project Overview
This project predicts whether a Spotify track will be a **HIT or NOT HIT** based on its **audio features** like Danceability, Energy, Valence, Tempo, etc.  
I built a **Random Forest Classifier achieving 99% accuracy** and deployed it as an interactive **Streamlit Web App**.

---

## 🧑‍💻 Beginner's Guide: How I Built This (Step-by-Step)
1. **Problem Understanding** — Predict song popularity based on musical features.
2. **Dataset** — Used Spotify Tracks dataset containing:
   - Features like danceability, energy, loudness, speechiness, valence, tempo, etc.
   - Target column: `Hit` (1 if Popularity > 70, else 0).
3. **Data Preprocessing**
   - Selected 9 core numerical features.
   - Scaled the features using `StandardScaler`.
4. **Model Training**
   - Tried multiple models: Logistic Regression, KNN, Decision Tree, Random Forest.
   - Random Forest achieved the best accuracy: **99%**.
5. **Model Deployment**
   - Built a **Streamlit App** for real-time Hit/Non-Hit Prediction.
6. **Phase 2 (Coming Soon)**
   - Content-Based Song Recommendation System.

---

## 🏆 Key Features
- **Interactive Web App** for predicting whether a song will be a Hit or Not.
- Compared multiple Machine Learning models.
- Achieved **99% accuracy with Random Forest Classifier**.
- Beginner-friendly code structure.
- Ready for future extensions like **Recommendation Engine**.

---

## 📈 Model Performance
| Model                | Accuracy |
|----------------------|---------:|
| Logistic Regression   | 97%      |
| K-Nearest Neighbors   | 96%      |
| Decision Tree         | 98%      |
| **Random Forest**     | **99%**  |

---

## How to Run Locally
### 1. Clone the Repository
```bash
git clone https://github.com/your-username/spotify-hit-predictor.git
cd spotify-hit-predictor
```

2. Install Required Packages
```bash
pip install -r requirements.txt
```

3. Run the Streamlit App
```bash
streamlit run app.py
```

### Project Structure

```bash
spotify-hit-predictor/
├── app.py                    # Streamlit App Code
├── hit_classifier_rf.pkl     # Trained Random Forest Model
├── scaler.pkl                # StandardScaler Object
├── SpotifyFeatures.csv       # Dataset
├── requirements.txt          # Python Packages
├── spotify.ipynb             # Jupyter Notebook File
├── README.md                 # This File
```

### Highlights of This Project
Full Machine Learning Pipeline from scratch.
End-to-End Deployment with Streamlit.
Achieved 99% prediction accuracy.
Simple yet powerful — Perfect for learning ML Deployment.
Scalable architecture for future AI Product features.

