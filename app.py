import streamlit as st
import requests
import hashlib
import re
import secrets
import string

# Check password strength level and details
def check_strength(password):
    length = len(password)
    has_digit = re.search(r"\d", password) is not None
    has_upper = re.search(r"[A-Z]", password) is not None
    has_lower = re.search(r"[a-z]", password) is not None
    has_special = re.search(r"[\W_]", password) is not None

    checks = {
        "✅ Minimum 8 characters": length >= 8,
        "✅ Contains a number": has_digit,
        "✅ Contains an uppercase letter": has_upper,
        "✅ Contains a lowercase letter": has_lower,
        "✅ Contains a special character": has_special,
    }

    score = sum(checks.values())

    if length < 8:
        strength = "Very Weak"
        percent = 20
        color = "red"
    elif score <= 2:
        strength = "Weak"
        percent = 40
        color = "orange"
    elif score == 3 or score == 4:
        strength = "Moderate"
        percent = 60
        color = "yellow"
    else:
        strength = "Strong"
        percent = 100
        color = "green"

    return strength, percent, color, checks

# Check if password was leaked
def check_password_leak(password):
    sha1 = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    prefix = sha1[:5]
    suffix = sha1[5:]

    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    res = requests.get(url)

    if res.status_code != 200:
        return -1

    hashes = (line.split(":") for line in res.text.splitlines())
    for h, count in hashes:
        if h == suffix:
            return int(count)
    return 0

# Generate strong password 
def generate_strong_password(length=12):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    while True:
        pwd = ''.join(secrets.choice(alphabet) for _ in range(length))
        if (re.search(r"\d", pwd) and re.search(r"[A-Z]", pwd) and
            re.search(r"[a-z]", pwd) and re.search(r"[\W_]", pwd)):
            return pwd

# Streamlit UI 
st.set_page_config(page_title="Password Strength & Leak Checker", layout="centered")
st.title("🔐 Password Strength & Leak Checker")
st.write("Check password security and get suggestions to improve it.")

password = st.text_input("Enter your password", type="password")

if password:
    # Strength analysis
    st.subheader("Strength Analysis")
    strength, percent, color, checks = check_strength(password)

    st.markdown(f"**Strength:** `{strength}`")
    st.progress(percent)

    for msg, passed in checks.items():
        if passed:
            st.success(msg)
        else:
            st.warning("❌ " + msg[2:])

    # Leak check
    st.subheader("🚨 Leak Check")
    with st.spinner("Checking against data breaches..."):
        count = check_password_leak(password)

    if count == -1:
        st.error("❌ API error. Please try again later.")
    elif count == 0:
        st.success("✅ This password has NOT been found in any known data breaches.")
    else:
        st.error(f"⚠️ This password has been found in {count:,} data breaches. Avoid using it!")

    st.markdown("---")
    st.info("💡 Tip: Use a password manager and avoid reusing passwords.")

# Suggested passwords
if password:
    st.subheader("🛡️ Strong Password Suggestions")
    st.markdown("Here are some strong passwords you can use:")

    for i in range(3):
        new_pwd = generate_strong_password()
        st.code(new_pwd)

