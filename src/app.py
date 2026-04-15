"""
CloudShield - Main Application
Zero-Trust Access Control Platform for AWS S3
"""

import streamlit as st
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.iam_manager import IAMPolicyManager, POLICY_TEMPLATES
from src.s3_manager import S3BucketManager

# Page config
st.set_page_config(
    page_title="CloudShield",
    page_icon="🛡️",
    layout="wide"
)

# Title
st.title("🛡️ CloudShield")
st.markdown("### Zero-Trust Access Control Platform for AWS S3")

# Check AWS credentials
from dotenv import load_dotenv
load_dotenv()
aws_configured = os.getenv("AWS_ACCESS_KEY_ID") is not None

# Tabs
tab1, tab2, tab3 = st.tabs(["🏠 Dashboard", "📦 S3 Buckets", "🔐 IAM Policies"])

# Dashboard Tab
with tab1:
    st.header("📊 Dashboard")
    
    if aws_configured:
        st.success("✅ AWS credentials configured")
        try:
            s3 = S3BucketManager()
            buckets = s3.list_buckets()
            st.metric("Total Buckets", len(buckets))
        except Exception as e:
            st.error(f"❌ Error connecting to AWS: {e}")
    else:
        st.warning("⚠️ AWS credentials not configured. Create .env file")

# S3 Buckets Tab
with tab2:
    st.header("📦 S3 Bucket Management")
    
    if aws_configured:
        s3 = S3BucketManager()
        buckets = s3.list_buckets()
        
        if buckets:
            st.subheader("Your Buckets")
            for bucket in buckets:
                st.write(f"📦 {bucket['Name']}")
        else:
            st.info("No buckets found")
    else:
        st.error("❌ AWS credentials not configured")

# IAM Policies Tab
with tab3:
    st.header("🔐 IAM Policy Management")
    
    if aws_configured:
        st.subheader("Policy Templates")
        for name in POLICY_TEMPLATES.keys():
            st.code(f"Template: {name}", language="text")
    else:
        st.error("❌ AWS credentials not configured")

st.caption("🛡️ CloudShield - Zero-Trust Access Control Platform")
