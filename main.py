from src.f1_performance.session_loader import load_session

def main():

        session = load_session(
            year=2025,
            grand_prix="Monza",
            session_type="Q"
        )

        print("\nSESSION INFORMATION")
        print("-------------------")
        print("Event:", session.event["EventName"])
        print("Session:", session.name)
        print("Number of laps:", len(session.laps))

        print("\nDRIVERS")
        print(session.laps["Driver"].dropna().unique())            

if __name__ == "__main__":
    main()  
