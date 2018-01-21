from .faculty import FacultySerializer
from .inbox import InboxSerializer
from .letter import LetterSerializer
from .remark import RemarkSerializer
from .student import StudentSerializer
from .user import UserSerializer

faculty_serializer = FacultySerializer()
inbox_serializer = InboxSerializer()
letter_serializer = LetterSerializer()
remark_serializer = RemarkSerializer()
student_serializer = StudentSerializer()
user_serializer = StudentSerializer()
