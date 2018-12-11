#!/usr/bin/env python
import logging
import math

from duckietown_challenges import wrap_evaluator, ChallengeEvaluator, InvalidSubmission

logging.basicConfig()
logger = logging.getLogger('evaluator')
logger.setLevel(logging.DEBUG)


class Evaluator(ChallengeEvaluator):

    def prepare(self, cie):
        cie.set_challenge_parameters({'dummy':1})

    def score(self, cie):
        solution_output = cie.get_solution_output_dict()
	'''
	Define here how scoring of a solution is done.
	'''
	temp = solution_output['data']
	score = 2*temp
        cie.set_score('score1', score, 'blurb')


if __name__ == '__main__':
    wrap_evaluator(Evaluator())
