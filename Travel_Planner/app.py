import streamlit as st
from prompts import system_prompts, user_prompts
from utils import itinerary_utils 

def main():
    """
    Streamlit app for AI Travel Planner.
    """

    st.title("AI Travel Planner ✈️")
    st.write("---")

    st.subheader("Tell us about your dream trip:")

    destination = st.text_input("Enter your destination:")
    trip_duration = st.number_input("How many days will you be traveling?", min_value=1, step=1)
    budget = st.selectbox("What is your budget?", options=["Luxury", "Moderate", "Budget", "Backpacker"])
    interests = st.multiselect(
        "What are your interests?",
        options=["History", "Food", "Art", "Nature", "Adventure", "Relaxation", "Nightlife", "Shopping"]
    )

    if st.button("Plan My Trip"):
        if destination:
            st.write("---")
            st.subheader(f"Planning your trip to {destination}")

            # Example: Get activity suggestions (replace with your own logic)
            activity_suggestions = itinerary_utils.suggest_activities(destination, interests) 

            # Example: Build a basic daily schedule (replace with your own logic)
            daily_schedule = itinerary_utils.build_daily_schedule(activity_suggestions, trip_duration)

            # Create a basic itinerary string (replace with your desired formatting)
            itinerary = f"**{destination} Itinerary**\n"
            itinerary += f"**Trip Duration:** {trip_duration} days\n"
            itinerary += f"**Budget:** {budget}\n"
            itinerary += f"**Interests:** {', '.join(interests)}\n\n"
            itinerary += "**Daily Schedule:**\n"
            for day, activities in daily_schedule.items():
                itinerary += f"**Day {day}:** {', '.join(activities)}\n"

            st.write(itinerary)
        else:
            st.warning("Please enter a destination.")

if __name__ == "__main__":
    main()