import streamlit as st

st.set_page_config(page_title="AI Content System")

st.title("AI Multi-Agent Content Automation System")

product = st.text_input("Enter Product / Description")

if st.button("Run System"):

    # ------------------ PLANNER ------------------
    st.subheader("Planner Agent")
    plan = [
        "1. Generate Blog",
        "2. Generate Social Posts",
        "3. Generate FAQ",
        "4. Check Compliance",
        "5. Fix Issues if needed",
        "6. Optimize Content",
        "7. Final Output"
    ]
    for step in plan:
        st.write(step)

    # ------------------ GENERATOR ------------------
    st.subheader("Generator Agent")

    blog = f"{product} is the best product in the market. It gives guaranteed results and improves life."

    social = [
        f"Try {product} today!",
        f"{product} will change your life!",
        f"Don't miss {product}!"
    ]

    faq = f"What is {product}? It is a product designed to improve your daily routine."

    st.write("Blog:", blog)
    st.write("Social Posts:", social)
    st.write("FAQ:", faq)

    # ------------------ COMPLIANCE ------------------
    st.subheader("Compliance Agent")

    issues = []

    if "best" in blog.lower():
        issues.append("Use of 'best' is not allowed")

    if "guaranteed" in blog.lower():
        issues.append("Use of 'guaranteed' is risky")

    if issues:
        st.error("Issues found:")
        for i in issues:
            st.write("-", i)

        # Auto Fix
        blog = blog.replace("best", "high-quality")
        blog = blog.replace("guaranteed", "effective")

        st.success("System auto-corrected the content")
    else:
        st.success("No issues found")

    # ------------------ OPTIMIZER ------------------
    st.subheader("Optimizer Agent")

    blog = blog + " This version is optimized for clarity, tone, and engagement."

    # ------------------ FINAL OUTPUT ------------------
    st.subheader("Final Output")

    st.write("Final Blog:", blog)
    st.write("Final Social:", social)
    st.write("Final FAQ:", faq)

    # ------------------ AUDIT TRAIL ------------------
    st.subheader("Audit Trail")

    logs = [
        "Planner created workflow",
        "Generator created content",
        "Compliance checked and fixed issues",
        "Optimizer improved output",
        "Final result generated"
    ]

    for log in logs:
        st.write(log)