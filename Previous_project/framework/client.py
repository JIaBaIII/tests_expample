import requests as r

from config import API_URL

URL = API_URL


class Client:

	def _get(self, path: str, headers):
		return r.get(url=URL + path, headers=headers)

	def _post(self, path: str, json, headers, data, files):
		return r.post(url=URL + path, json=json, headers=headers, data=data, files=files)

	def _put(self, path: str, json, headers, data, files):
		return r.put(url=URL + path, json=json, headers=headers, data=data, files=files)

	def _delete(self, path: str, headers):
		return r.delete(url=URL + path, headers=headers)

	# Question API

	def get_answer_comment(self, answer_id, headers=None):
		return self._get(path=f'/v1/GetAnswerComments/{answer_id}', headers=headers)

	def get_question_answer(self, question_id, headers=None):
		return self._get(path=f'/v1/GetQuestionAnswers/{question_id}', headers=headers)

	def get_answers(self, answer_id, headers=None):
		return self._get(path=f'/v1/answers/{answer_id}', headers=headers)

	def get_questions(self, question_id, headers=None):
		return self._get(path=f'/v1/questions/{question_id}', headers=headers)

	def get_f_feed(self, headers=None):
		return self._get(path=f'/v1/feed', headers=headers)

	def get_question_unpublish(self, question_id, headers=None):
		return self._get(path=f'/_/v1/question/{question_id}/unpublish', headers=headers)

	def get_question_publish(self, question_id, headers=None):
		return self._get(path=f'/_/v1/question/{question_id}/publish', headers=headers)

	def post_answer_create(self, json=None, headers=None, data=None, files=None):
		return self._post(path=f'/_/v1/answers', json=json, headers=headers, data=data, files=files)

	def post_question_create(self, json=None, headers=None, data=None, files=None):
		return self._post(path=f'/_/v1/questions', json=json, data=data, headers=headers, files=files)

	def put_question_publish(self, question_id, json=None, headers=None, data=None, files=None):
		return self._put(
			path=f'/_/v1/questions/{question_id}/publish', json=json, data=data, headers=headers, files=files)

	def put_question_update(self, question_id, json=None, headers=None, data=None, files=None):
		return self._put(path=f'/_/v1/questions/{question_id}', json=json, data=data, headers=headers, files=files)

	def delete_question(self, question_id, headers=None):
		return self._delete(path=f'/_/v1/questions/{question_id}', headers=headers)

	def delete_answer(self, answer_id, headers=None):
		return self._delete(path=f'/_/v1/answers/{answer_id}', headers=headers)

	def post_login_user(self, json=None, headers=None, data=None, files=None):
		return self._post(path=f'/v1/login', json=json, headers=headers, data=data, files=files)

	def post_question_status(self, question_id, json=None, headers=None, data=None, files=None):
		return self._post(path=f'/_/v1/questions/{question_id}/status', json=json, headers=headers, data=data, files=files)

	# Article API

	def get_article(self, article_id, headers=None):
		return self._get(path=f'/v1/articles/{article_id}', headers=headers)

	def put_article_publish(self, article_id, json=None, headers=None, data=None, files=None):
		return self._put(path=f'/_/v1/articles/{article_id}/publish', json=json, data=data, headers=headers, files=files)

	def get_article_unpublish(self, article_id, headers=None):
		return self._get(path=f'/_/v1/articles/{article_id}/unpublish', headers=headers)

	def get_comments_article(self, comment_id, headers=None):
		return self._get(path=f'/v1/articles/comments/{comment_id}', headers=headers)

	def post_article_create(self, json=None, headers=None, data=None, files=None):
		return self._post(path=f'/_/v1/articles', json=json, headers=headers, data=data, files=files)

	def post_article_update(self, json=None, headers=None, data=None, files=None):
		return self._post(path=f'/_/v1/articles/update', json=json, headers=headers, data=data, files=files)

	def post_article_upload(self, json=None, headers=None, data=None, files=None):
		return self._post(path=f'/_v2/articles/upload', json=json, headers=headers, data=data, files=files)

	def post_article_comment_find(self, json=None, headers=None, data=None, files=None):
		return self._post(path=f'/v1/articles/comments/find', json=json, headers=headers, data=data, files=files)

	def post_article_find(self, json=None, headers=None, data=None, files=None):
		return self._post(path=f'/v1/articles/find', json=json, headers=headers, data=data, files=files)

	def delete_article(self, article_id, headers=None):
		return self._delete(path=f'/_/v1/articles/{article_id}', headers=headers)

	# Feed API

	def get_feed(self, offset, limit, headers=None):
		return self._get(
			path=f'/v1.2/feed?Offset={offset}&Limit={limit}', headers=headers)

	# Access Service API

	def get_info(self, headers=None):
		return self._get(path=f'/_/v1/info', headers=headers)

	def get_logout(self, headers=None):
		return self._get(path=f'/_/v1/logout', headers=headers)

	def get_ticket(self, headers=None):
		return self._get(path=f'/_/v1/ticket', headers=headers)

	def post_sign_up_user(self, json=None, data=None, headers=None, files=None):
		return self._post(path=f'/v1/sign-up', json=json, data=data, headers=headers, files=files)

	def post_login(self, json=None, data=None, headers=None, files=None):
		return self._post(path=f'/v1/login', json=json, data=data, headers=headers, files=files)

	def get_ws_connect(self, ticket, headers=None):
		return r.get(url=f'ws://toci-test-01.aurora:8080/v2/ws?Ticket={ticket}', headers=headers)

	# Interaction API

	def post_complain(self, json=None, headers=None, data=None, files=None):
		return self._post(path=f'/_/v1/complain', json=json, headers=headers, data=data, files=files)

	def put_downvote(self, json=None, headers=None, data=None, files=None):
		return self._put(path=f'/_/v1/downvote', json=json, headers=headers, data=data, files=files)

	def put_upvote(self, json=None, headers=None, data=None, files=None):
		return self._put(path=f'/_/v1/upvote', json=json, headers=headers, data=data, files=files)

	def post_viewed(self, json=None, headers=None, data=None, files=None):
		return self._post(path=f'/_/v1/viewed', json=json, headers=headers, data=data, files=files)

	def post_vote_delete(self, json=None, headers=None, data=None, files=None):
		return self._post(path=f'/_/v1/vote/delete', json=json, headers=headers, data=data, files=files)

	def post_get_likes(self, json=None, headers=None, data=None, files=None):
		return self._post(path=f'/v1/likes', json=json, headers=headers, data=data, files=files)

	def post_get_views(self, json=None, headers=None, data=None, files=None):
		return self._post(path=f'/v1/views', json=json, headers=headers, data=data, files=files)

	def post_get_votes(self, json=None, headers=None, data=None, files=None):
		return self._post(path=f'/v1/votes', json=json, headers=headers, data=data, files=files)

	# Profile API

	def post_personal_status(self, json=None, headers=None, data=None, files=None):
		return self._post(path=f'/_/v1/personal/status', json=json, headers=headers, data=data, files=files)

	def post_personal_update(self, json=None, headers=None, data=None, files=None):
		return self._post(path=f'/_/v1/personal/update', json=json, headers=headers, data=data, files=files)

	def post_avatar_upload(self, files=None, headers=None, json=None, data=None):
		return self._post(path=f'/_/v2/avatar/upload', data=data, headers=headers, json=json, files=files)

	def get_avatar(self, headers=None):
		return self._get(path=f'/v1/avatar', headers=headers)

	def get_avatar_user_id(self, user_id, headers=None):
		return self._get(path=f'/v1/avatar?UserID={user_id}', headers=headers)

	def get_personal_user_id(self, user_id=None, headers=None):
		return self._get(path=f'/v1/personal/{user_id}', headers=headers)

	# Followers API

	def get_follow(self, element_id=None, headers=None):
		return self._get(path=f'/_/v1/follow/{element_id}', headers=headers)

	def get_unfollow(self, element_id=None, headers=None):
		return self._get(path=f'/_/v1/unfollow/{element_id}', headers=headers)

	# Notifications API

	def get_notifications(self, headers=None):
		return self._get(path=f'/_/v1/notifications', headers=headers)

	def get_notifications_delivered(self, notification_id=None, headers=None):
		return self._get(path=f'/_/v1/notifications/{notification_id}/delivered', headers=headers)

	# Comment API

	def post_comment(self, json=None, headers=None, data=None, files=None):
		return self._post(path=f'/_/v1/comments', data=data, json=json, headers=headers, files=files)

	def delete_comment(self, comment_id, headers=None):
		return self._delete(path=f'/_/v1/comments/{comment_id}', headers=headers)
