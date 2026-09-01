from crew import blog_crew


inputs = {
    "topic": "Artificial Intelligence in Business"
}


result = blog_crew.kickoff(
    inputs=inputs
)


print("\n")
print("=" * 60)
print("FINAL BLOG")
print("=" * 60)
print(result)