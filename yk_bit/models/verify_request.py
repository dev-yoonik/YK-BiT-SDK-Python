# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401
from typing import List, Dict  # noqa: F401
from yk_utils.models import Model
from yk_utils.models import deserialization


class VerifyRequest(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, capture_time_out: float=10.0, reference_image: str=None, matching_score_threshold: float=0.4, anti_spoofing: bool=True, live_quality_analysis: bool=False, reference_quality_analysis: bool=False):  # noqa: E501
        """VerifyRequest - a model defined in Swagger

        :param capture_time_out: The capture_time_out of this VerifyRequest.  # noqa: E501
        :type capture_time_out: float
        :param reference_image: The reference_image of this VerifyRequest.  # noqa: E501
        :type reference_image: str
        :param matching_score_threshold: The matching_score_threshold of this VerifyRequest.  # noqa: E501
        :type matching_score_threshold: float
        :param anti_spoofing: The anti_spoofing of this VerifyRequest.  # noqa: E501
        :type anti_spoofing: bool
        :param live_quality_analysis: The live_quality_analysis of this VerifyRequest.  # noqa: E501
        :type live_quality_analysis: bool
        :param reference_quality_analysis: The reference_quality_analysis of this VerifyRequest.  # noqa: E501
        :type reference_quality_analysis: bool
        """
        self.swagger_types = {
            'capture_time_out': float,
            'reference_image': str,
            'matching_score_threshold': float,
            'anti_spoofing': bool,
            'live_quality_analysis': bool,
            'reference_quality_analysis': bool
        }

        self.attribute_map = {
            'capture_time_out': 'capture_time_out',
            'reference_image': 'reference_image',
            'matching_score_threshold': 'matching_score_threshold',
            'anti_spoofing': 'anti_spoofing',
            'live_quality_analysis': 'live_quality_analysis',
            'reference_quality_analysis': 'reference_quality_analysis'
        }

        self._capture_time_out = capture_time_out
        self._reference_image = reference_image
        self._matching_score_threshold = matching_score_threshold
        self._anti_spoofing = anti_spoofing
        self._live_quality_analysis = live_quality_analysis
        self._reference_quality_analysis = reference_quality_analysis

    @classmethod
    def from_dict(cls, dikt) -> 'VerifyRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The verify_request of this VerifyRequest.  # noqa: E501
        :rtype: VerifyRequest
        """
        return deserialization.deserialize_model(dikt, cls)

    @property
    def capture_time_out(self) -> float:
        """Gets the capture_time_out of this VerifyRequest.

        Capture timeout in seconds.  # noqa: E501

        :return: The capture_time_out of this VerifyRequest.
        :rtype: float
        """
        return self._capture_time_out

    @capture_time_out.setter
    def capture_time_out(self, capture_time_out: float):
        """Sets the capture_time_out of this VerifyRequest.

        Capture timeout in seconds.  # noqa: E501

        :param capture_time_out: The capture_time_out of this VerifyRequest.
        :type capture_time_out: float
        """

        self._capture_time_out = capture_time_out

    @property
    def reference_image(self) -> str:
        """Gets the reference_image of this VerifyRequest.

        JPG base 64 string reference face image obtained from identification document or any other source.  # noqa: E501

        :return: The reference_image of this VerifyRequest.
        :rtype: str
        """
        return self._reference_image

    @reference_image.setter
    def reference_image(self, reference_image: str):
        """Sets the reference_image of this VerifyRequest.

        JPG base 64 string reference face image obtained from identification document or any other source.  # noqa: E501

        :param reference_image: The reference_image of this VerifyRequest.
        :type reference_image: str
        """

        self._reference_image = reference_image

    @property
    def matching_score_threshold(self) -> float:
        """Gets the matching_score_threshold of this VerifyRequest.

        Matching score threshold used to verify matching between live and reference image.  # noqa: E501

        :return: The matching_score_threshold of this VerifyRequest.
        :rtype: float
        """
        return self._matching_score_threshold

    @matching_score_threshold.setter
    def matching_score_threshold(self, matching_score_threshold: float):
        """Sets the matching_score_threshold of this VerifyRequest.

        Matching score threshold used to verify matching between live and reference image.  # noqa: E501

        :param matching_score_threshold: The matching_score_threshold of this VerifyRequest.
        :type matching_score_threshold: float
        """

        self._matching_score_threshold = matching_score_threshold

    @property
    def anti_spoofing(self) -> bool:
        """Gets the anti_spoofing of this VerifyRequest.

        Activate anti-spoofing detection.  # noqa: E501

        :return: The anti_spoofing of this VerifyRequest.
        :rtype: bool
        """
        return self._anti_spoofing

    @anti_spoofing.setter
    def anti_spoofing(self, anti_spoofing: bool):
        """Sets the anti_spoofing of this VerifyRequest.

        Activate anti-spoofing detection.  # noqa: E501

        :param anti_spoofing: The anti_spoofing of this VerifyRequest.
        :type anti_spoofing: bool
        """

        self._anti_spoofing = anti_spoofing

    @property
    def live_quality_analysis(self) -> bool:
        """Gets the live_quality_analysis of this VerifyRequest.

        Activate ISO/ICAO-19794-5 face quality compliance checks on the live face images.  # noqa: E501

        :return: The live_quality_analysis of this VerifyRequest.
        :rtype: bool
        """
        return self._live_quality_analysis

    @live_quality_analysis.setter
    def live_quality_analysis(self, live_quality_analysis: bool):
        """Sets the live_quality_analysis of this VerifyRequest.

        Activate ISO/ICAO-19794-5 face quality compliance checks on the live face images.  # noqa: E501

        :param live_quality_analysis: The live_quality_analysis of this VerifyRequest.
        :type live_quality_analysis: bool
        """

        self._live_quality_analysis = live_quality_analysis

    @property
    def reference_quality_analysis(self) -> bool:
        """Gets the reference_quality_analysis of this VerifyRequest.

        Activate ISO/ICAO-19794-5 face quality compliance checks on the reference_image.  # noqa: E501

        :return: The reference_quality_analysis of this VerifyRequest.
        :rtype: bool
        """
        return self._reference_quality_analysis

    @reference_quality_analysis.setter
    def reference_quality_analysis(self, reference_quality_analysis: bool):
        """Sets the reference_quality_analysis of this VerifyRequest.

        Activate ISO/ICAO-19794-5 face quality compliance checks on the reference_image.  # noqa: E501

        :param reference_quality_analysis: The reference_quality_analysis of this VerifyRequest.
        :type reference_quality_analysis: bool
        """

        self._reference_quality_analysis = reference_quality_analysis
