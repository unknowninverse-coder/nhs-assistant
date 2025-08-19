import streamlit as st

# Helper Functions
def show_recommendation(service_type, title, description, details):
    st.markdown("## " + title)
    st.markdown(f"**Service:** {service_type}")
    st.write(description)
    with st.expander("Details"):
        st.write(details)
    st.markdown("---")

# Symptom Flow Trees
def sore_throat_flow():
    choice = st.radio("How long have you had these symptoms?", 
                      ["Less than a week", "More than a week"])

    if choice == "Less than a week":
        breath_choice = st.radio("Are you having any difficulty breathing?", 
                                 ["No, I'm not", "Yes, I am"])
        if breath_choice == "No, I'm not":
            show_recommendation(
                "Self-Care",
                "Recommendation: Self-Care",
                "For a recent sore throat with no breathing issues, self-care at home is usually best option to proceed with.",
                "Rest, drink plenty of water, and you can use over-the-counter/prescribed lozenges or pain relief. If your symptoms don't improve in a week or get worse, please contact your local GP."
            )
        else:
            emergency_flow("difficulty breathing")
    else:
        worse_choice = st.radio("Since it's been over a week, are your symptoms getting worse?", 
                                ["No, they're pretty much the same", "Yes, they are getting worse"])
        show_recommendation(
            "GP",
            "Recommendation: Contact Your local GP",
            "As your symptoms have lasted for a while, it's best to speak with a GP before your condition could potentially worsen.",
            "They can properly diagnose the issue and suggest a course of treatment. Please book a non-urgent appointment with your GP surgery."
        )

def skin_rash_flow():
    choice = st.radio("Is the rash accompanied by a fever or difficulty breathing?", 
                      ["No, just the rash", "Yes, I have a fever", "Yes, I can't breathe well"])
    if choice == "No, just the rash":
        itchy_choice = st.radio("Does the rash feel itchy or irritated?", 
                                ["Yes, it's itchy", "No, not really"])
        if itchy_choice == "Yes, it's itchy":
            show_recommendation(
                "Pharmacy",
                "Recommendation: Visit a Pharmacy",
                "A local pharmacist can help with itchy or irritated rashes.",
                "They can look at the rash and recommend over-the-counter creams or antihistamines. They will tell you whether or not you need to see a GP."
            )
        else:
            show_recommendation(
                "GP",
                "Recommendation: Contact Your GP",
                "A rash that isn't itchy should be checked by a doctor to be safe.",
                "Please book a non-urgent appointment with your GP surgery to get a proper diagnosis."
            )
    elif choice == "Yes, I have a fever":
        show_recommendation(
            "GP",
            "Recommendation: Contact Your GP",
            "A rash accompanied by a fever should be checked by a doctor.",
            "Please book a non-urgent appointment with your GP surgery to get a proper diagnosis."
        )
    else:
        emergency_flow("a rash and difficulty breathing")

def headache_flow():
    choice = st.radio("How severe is your headache?", 
                      ["Mild", "Moderate", "Severe"])

    if choice == "Mild":
        duration_choice = st.radio("How long have you had this headache?", 
                                   ["Less than a day", "More than a day"])
        if duration_choice == "Less than a day":
            show_recommendation(
                "Self-Care",
                "Recommendation: Self-Care",
                "For a mild headache lasting less than a day, self-care at home is usually sufficient.",
                "Rest, stay hydrated, and consider over-the-counter pain relief like paracetamol or ibuprofen. If symptoms worsen or persist, contact your GP."
            )
        else:
            show_recommendation(
                "GP",
                "Recommendation: Contact Your GP",
                "A mild headache lasting more than a day should be checked by a doctor.",
                "Book a non-urgent appointment with your GP to rule out underlying causes."
            )

    elif choice == "Moderate":
        nausea_choice = st.radio("Are you experiencing nausea, vomiting, or visual disturbances?", 
                                 ["No", "Yes"])
        if nausea_choice == "No":
            show_recommendation(
                "Self-Care / GP",
                "Recommendation: Self-Care or GP Advice",
                "Moderate headaches without other symptoms can often be managed at home.",
                "Rest, hydration, and over-the-counter pain relief. If the headache persists for several days or worsens, see your GP."
            )
        else:
            show_recommendation(
                "GP",
                "Recommendation: Contact Your GP",
                "Moderate headache with nausea, vomiting, or visual disturbances may require medical attention.",
                "Please contact your GP for assessment and advice."
            )

    else:  # Severe
        emergency_symptoms = st.radio(
            "Do you have any of the following: sudden severe pain, weakness, slurred speech, confusion, fever, neck stiffness, or vision changes?", 
            ["No", "Yes"]
        )
        if emergency_symptoms == "Yes":
            emergency_flow("a severe headache with concerning symptoms")
        else:
            show_recommendation(
                "GP",
                "Recommendation: Contact Your GP",
                "A severe headache without classic emergency signs still warrants a doctor’s advice.",
                "Please contact your GP as soon as possible for assessment."
            )

def emergency_flow(symptom_description):
    show_recommendation(
        "A&E / 999",
        "Recommendation: Go to A&E or Call 999",
        f"Symptoms like {symptom_description} can be signs of a serious medical emergency.",
        "This requires immediate medical attention. Please go to your nearest A&E department or call 999 for an ambulance right away."
    )

# --- Main App ---
def main():
    st.title("NHS Virtual Assistant 🏥")
    st.write("⚠️ If this is a life-threatening emergency, please call **999** immediately. This service is NOT official and is for guidance only.")
    st.write("Produced by Jayden Siluvaimani")
    main_symptom = st.radio("What is your main symptom?", 
                            ["Sore Throat / Cold", "Skin Rash", "Headache", "Chest Pain"])

    if main_symptom == "Sore Throat / Cold":
        sore_throat_flow()
    elif main_symptom == "Skin Rash":
        skin_rash_flow()
    elif main_symptom == "Headache":
        headache_flow()
    elif main_symptom == "Chest Pain":
        emergency_flow("chest pain")

if __name__ == "__main__":
    main()



