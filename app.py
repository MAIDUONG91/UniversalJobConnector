from database.repository import JobRepository


def main():

    repository = JobRepository()

    print(f"Tổng số Job: {repository.count()}")

    print()

    for job in repository.get_all():

        print(job["id"])

        print(job["title"])

        print(job["company"])

        print(job["location"])

        print("-" * 50)

    repository.close()


if __name__ == "__main__":
    main()