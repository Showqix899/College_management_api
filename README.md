API ENDPOINTS

-> staff
  1.http://127.0.0.1:8000/staff/register/   -- register
  2.http://127.0.0.1:8000/staff/login/   -- login
  3.http://127.0.0.1:8000//staff/token/obtain/   -- generate a new jwt token
  4.http://127.0.0.1:8000/staff/token/refresh/   -- refresh jwt token
  5.http://127.0.0.1:8000//staff/logout/   -- logout

-> students
  1.http://127.0.0.1:8000/info -- for student post or get
  2.http://127.0.0.1:8000/info/<int:pk>/ -- for update delete

-> teachers
  1.http://127.0.0.1:8000/teachers -- for teacher post or get
  2.http://127.0.0.1:8000/teachers/<int:pk>/ -- for teacher update and delete
  3.http://127.0.0.1:8000/subjects -- for subject post or get
  4.http://127.0.0.1:8000/subjects/<int:pk>/ -- for subjects delete and update

-> result
  1.http://127.0.0.1:8000/result/student_result -- for post and get
  2.http://127.0.0.1:8000/resutl/student_result/<int:pk> -- for update and delete
  3.http://127.0.0.1:8000/student_reuslt_detail/<int:pk> -- for get detail of single student result and it's details
  
