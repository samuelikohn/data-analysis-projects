import pandas as pd
from matplotlib import pyplot as plt, colors as mcolors, patches as mpatches

df = pd.read_csv("Trends_in_Job_Application_Methods.csv")

# Give the columns shorter but still descriptive names
df.rename(
    columns = {
        "What is your current employment status?": "Employment Status",
        "How do you typically search for job opportunities?": "Job Search Method",
        "Which online platforms do you use most frequently to search for jobs?": "Platform",
        "How do you prefer to submit your resume to potential employers?": "Application Submission Method",
        "Do you use social media platforms as part of your job search strategy?": "Social Media Use",
        "How influential do you believe your social media presence is in the job application process?": "Importance of Social Media Influence",
        "How often do you attend networking events or job fairs to explore job opportunities?": "Networking Frequency",
        "How frequently do you rely on personal or professional connections to learn about job opportunities?": "Personal + Professional Connection Frequency",
        "Have you ever received a job referral that led to a successful application?": "Job Referral Success",
        "How important do you believe having a strong online presence (e.g., personal website, portfolio) is in the job application process?": "Importance of Online Presence",
        "Have you ever been contacted by a recruiter based on your online presence?": "Recruiter Contact",
        "How often do you follow up with employers after submitting a job application?": "Application Follow-Up Frequency",
        "What information in a job listing is most important to you when deciding to apply?": "Top Job Criterion"
    },
    inplace = True
)

# Create color list
COLORS = mcolors.TABLEAU_COLORS
COLORS.update({'m': (0.75, 0, 0.75)}) # Tableau color list is too short, add magenta to the color list as it's different from all existing colors

# List categorical columns that influence employment status
categories = df.columns.tolist()[3:] # Removes first 3 columns: Gender, Age Range, & Employment Status

# Remove numerical columns
categories.remove("Importance of Social Media Influence")
categories.remove("Importance of Online Presence")

# Create plots
for category in categories:

    # Define color dict
    colors = {k: v for (k, v) in zip(df[category].unique(), COLORS)}

    fig = plt.figure() # Set figure for plots
    i = 1 # Set index for subsplots

    # Configure each subplot
    for employment_state in df["Employment Status"].unique():
        ax = plt.subplot(2, 2, i)
        vals = df[df["Employment Status"] == employment_state][category]
        ax.pie(vals.value_counts(), autopct="%1.1f%%", colors=[colors[k] for k in vals.unique()])
        ax.set_title(employment_state, fontdict={"size": 10})
        i += 1

    # Configure super plot
    fig.suptitle(f"Percentage of {category} by Employment Status")
    handles = [mpatches.Patch(color=colors[k], label=k) for k in df[category].unique()] # Define custom handles for the legend
    fig.legend(loc="lower right", handles=handles)
    fig.tight_layout()

    # Set to fullscreen for visibility
    manager = plt.get_current_fig_manager()
    manager.window.showMaximized()
    plt.show()

    # Save figure as png
    fig.savefig(category + ".png")

# Create histograms of numerical data
num_cats = ["Importance of Social Media Influence", "Importance of Online Presence"]

# Create plots
for num_cat in num_cats:

    fig = plt.figure() # Create figure for subplots
    i = 1 # Set index for subplots

    # Configure subplots
    for employment_state in df["Employment Status"].unique():
        ax = plt.subplot(2, 2, i)
        vals = df[df["Employment Status"] == employment_state][num_cat]
        ax.hist(vals, bins=[0, 2, 4, 6, 8, 10])
        ax.set_title(employment_state, fontdict={"size": 10})
        ax.set_xlabel("Personal Ranking")
        ax.set_ylabel("Count")
        i += 1
        
    # Confiugure super plot
    fig.suptitle(f"Distribution of {num_cat} by Employment Status")
    fig.tight_layout()

    # Set to fullscreen for visibility
    manager = plt.get_current_fig_manager()
    manager.window.showMaximized()

    # Save figure as png
    plt.show()
    fig.savefig(num_cat + ".png")
