# Duke Generative AI Hackathon

### Inspiration
There is a shared realization that in today's fast-paced, information-driven world, traditional learning methods are struggling to keep up. We witnessed the struggles of students overwhelmed by lengthy lectures, professionals trying to upskill, and lifelong learners craving knowledge. The vast sea of video content, while rich in information, became a daunting obstacle. It was clear that to bridge this formidable 'learning gap,' a new approach was essential. We understood that the very medium that presented a challenge—video content—could also hold the solution. And so, we set out to create a tool that would empower every learner to unlock the full potential of video-based education. LumoScribe doesn't just change how you learn; it redefines how you engage with knowledge.

### What it does
Our platform empowers users in their learning journey, starting with seamless video uploads that are swiftly transcribed into easily digestible text.

**Transcription:** Videos are converted into well-structured text, giving users the freedom to read, skim, or search through content quickly. This transformation facilitates a deeper understanding and engagement with the material.

**Flashcards:** LumoScribe takes this transcribed text and turns it into quick, accessible flashcards. These bite-sized, high-impact summaries allow users to review and reinforce key concepts in a flash, making revision efficient and effective.

**Concise Summaries:** In addition to flashcards, we offer concise, easy-to-digest summaries. These summaries distill the essence of video lectures, providing users with a clear, coherent overview of the material. No more sifting through hours of content; our tool condenses it for you.

**Quiz Questions:** LumoScribe goes beyond passive learning. We automatically generate a diverse range of quiz questions based on the video content. These quizzes test your knowledge and understanding, transforming passive viewing into active learning.

**Past Lecture Archive:** Your journey doesn't end when the video does. Our tool helps you organize and access past lectures and notes efficiently. It's a virtual library at your fingertips, ensuring that knowledge is readily available whenever you need it.

### How we built it?
ML: We used OpenAI's DaVinci model, a state-of-the-art natural language processing powerhouse, to transmute video content into meaningful text. For live transcription, we integrated Whisper, to ensure accurate and real-time conversion of spoken words into written text.
Database: Data storage was efficiently managed using MongoDB, guaranteeing the security and accessibility of user-generated content.
UI: We used Streamlit, a user-friendly interface development platform. This allowed us to provide users with a straightforward, visually appealing, and highly functional environment in which they could interact with our tool.

### Challenges
We experienced difficulties in achieving live transcription using Whisper, but we're currently improving this by integrating the Azure Speech-to-Text REST API. We also encountered issues with the API rate limit, hindering faster processing of videos and audios. Due to time limitations, we couldn't include document and video combined summarization, but it remains a priority feature for future development.

### Accomplishments
We're immensely proud of crafting a tool that not only empowers individuals to learn efficiently and effectively but also transforms the learning experience. Our seamless integration of multiple technologies guarantees a remarkably user-friendly experience, and during our research phase, we've not only received good feedback but see tangible evidence of our tool's potential positive impact on users' learning journeys.

### What we learned
We've realized our tool's capacity to reshape the learning landscape, catering to diverse educational needs and preferences. We've also gained valuable insights into artificial intelligence's potential in improving learning experiences. Moreover, we've come to appreciate the importance of user experience in making our tool an indispensable learning companion for people from diverse backgrounds. These insights fuel our ongoing commitment to delivering an exceptional educational solution.

### What's next for LumoScribe?
We're gearing up to enhance our tool significantly. This includes integrating combined document and video processing features. Moreover, we're broadening the tool's horizons to accept various document formats, ensuring maximum versatility for our users. We acknowledge the hurdles faced in Whisper's live transcription and are swiftly overcoming them by integrating the Azure Speech-to-Text REST API. This integration guarantees more precise and efficient live transcription, enhancing the overall user experience.

### Built With
- Python
- OpenAI
- Streamlit
