from pathlib import Path

from app.generators.image import generate_image
from app.generators.text import generate_text
from app.generators.video import generate_video


def main():
    prompt = "A futuristic city at sunset, cinematic lighting"

    text = generate_text(
        f"Write a short description for this image: {prompt}"
    )

    print("\nTEXT:")
    print(text)

    output_path = Path("outputs/images/generated.png")
    output_path.parent.mkdir(parents=True, exist_ok=True)

    generate_image(
        prompt=prompt,
        output_path=str(output_path),
    )
    generate_video(
        prompt=prompt,
        output_path=Path("outputs/videos/generated.mp4")
    )

    print(f"\nImage saved to: {output_path}")


if __name__ == "__main__":
    main()