from pydub import AudioSegment

# Function to compress audio
def compress_audio(input_file, bitrate='64k'):
    audio = AudioSegment.from_file(input_file)
    compressed_audio = audio.set_frame_rate(44100).set_channels(1)
    output_buffer = io.BytesIO()
    compressed_audio.export(output_buffer, format='mp3', bitrate=bitrate)
    return output_buffer.getvalue()

# Function to compress image
def compress_image(input_file, quality=50):
    img = Image.open(input_file)
    output_buffer = io.BytesIO()
    img_format = input_file.name.split(".")[-1].lower()
    
    if img_format not in ["jpg", "jpeg"]:
        st.warning("Only JPEG format is supported for compression. Converting the image to JPEG...")
        img = img.convert("RGB")
    
    img.save(output_buffer, format='JPEG', quality=quality)
    return output_buffer.getvalue()
