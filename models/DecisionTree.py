import streamlit as st
from sklearn.tree import DecisionTreeClassifier

# parameters of decision tree algorithm
# 1. max_depth
# 2. min_samples_split
# 3. min_samples_leaf
# 4. min_weight_fraction_leaf
# 5. max_features
# 6. random_state
# 7. max_leaf_nodes
# 8. min_impurity_decrease
# 9. class_weight
# 10. ccp_alpha

def dt_param_selector():
    criterion = st.selectbox("Criterion", ["gini", "entropy"])
    max_depth = st.number_input("Max Depth", min_value=1, value=3)
    min_samples_split = st.number_input("Min Samples Split", min_value=2, value=2)
    min_samples_leaf = st.number_input("Min Samples Leaf", min_value=1, value=1)
    min_weight_fraction_leaf = st.number_input("Min Weight Fraction Leaf", min_value=0.0, max_value=1.0, value=0.0)
    max_features = st.selectbox("Max Features", ["auto", "sqrt", "log2", None])
    random_state = st.number_input("Random State", min_value=0, value=0)
    max_leaf_nodes = st.number_input("Max Leaf Nodes", min_value=1, value=1)
    min_impurity_decrease = st.number_input("Min Impurity Decrease", min_value=0.0, value=0.0)
    class_weight = st.selectbox("Class Weight", ["balanced", "balanced_subsample", None])
    ccp_alpha = st.number_input("CCP Alpha", min_value=0.0, value=0.0)
    
    params = {
        "criterion": criterion,
        "max_depth": max_depth,
        "min_samples_split": min_samples_split,
        "min_samples_leaf": min_samples_leaf,
        "min_weight_fraction_leaf": min_weight_fraction_leaf,
        "max_features": max_features,
        "random_state": random_state,
        "max_leaf_nodes": max_leaf_nodes,
        "min_impurity_decrease": min_impurity_decrease,
        "class_weight": class_weight,
        "ccp_alpha": ccp_alpha
    }
    return DecisionTreeClassifier(**params)
    