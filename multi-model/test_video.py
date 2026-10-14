from app.generators.video import generate_video


def main():
    prompt = """
    A Old Indian Village at sunset, near an jungle animals moving between
    Trees and canopy, people walking through a clean street,
    cinematic camera movement, realistic lighting
    """

    output_path = generate_video(
        prompt=prompt,
        output_path="outputs/videos/test.mp4",
    )

    print(f"Video generated: {output_path}")


if __name__ == "__main__":
    main()