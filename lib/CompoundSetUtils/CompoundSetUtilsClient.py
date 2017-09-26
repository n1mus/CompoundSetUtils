# -*- coding: utf-8 -*-
############################################################
#
# Autogenerated by the KBase type compiler -
# any changes made here will be overwritten
#
############################################################

from __future__ import print_function
# the following is a hack to get the baseclient to import whether we're in a
# package or not. This makes pep8 unhappy hence the annotations.
try:
    # baseclient and this client are in a package
    from .baseclient import BaseClient as _BaseClient  # @UnusedImport
except:
    # no they aren't
    from baseclient import BaseClient as _BaseClient  # @Reimport


class CompoundSetUtils(object):

    def __init__(
            self, url=None, timeout=30 * 60, user_id=None,
            password=None, token=None, ignore_authrc=False,
            trust_all_ssl_certificates=False,
            auth_svc='https://kbase.us/services/authorization/Sessions/Login'):
        if url is None:
            raise ValueError('A url is required')
        self._service_ver = None
        self._client = _BaseClient(
            url, timeout=timeout, user_id=user_id, password=password,
            token=token, ignore_authrc=ignore_authrc,
            trust_all_ssl_certificates=trust_all_ssl_certificates,
            auth_svc=auth_svc)

    def compound_set_from_file(self, params, context=None):
        """
        CompoundSetFromFile
        string staging_file_path
        :param params: instance of type "compoundset_upload_params" ->
           structure: parameter "workspace_id" of String, parameter
           "staging_file_path" of String, parameter "compound_set_name" of
           String
        :returns: instance of type "compoundset_upload_results" -> structure:
           parameter "report_name" of String, parameter "report_ref" of
           String, parameter "compoundset_ref" of type "obj_ref"
        """
        return self._client.call_method(
            'CompoundSetUtils.compound_set_from_file',
            [params], self._service_ver, context)

    def compound_set_to_file(self, params, context=None):
        """
        CompoundSetToFile
        string compound_set_name
        string output_format
        :param params: instance of type "compoundset_download_params" ->
           structure: parameter "compound_set_ref" of String, parameter
           "output_format" of String
        :returns: instance of type "compoundset_download_results" ->
           structure: parameter "report_name" of String, parameter
           "report_ref" of String
        """
        return self._client.call_method(
            'CompoundSetUtils.compound_set_to_file',
            [params], self._service_ver, context)

    def compound_set_from_model(self, params, context=None):
        """
        CompoundSetFromModel
        required:
        string workspace_id
        string model_ref
        string compound_set_name
        :param params: instance of type "compoundset_from_model_params" ->
           structure: parameter "workspace_id" of String, parameter
           "model_ref" of String, parameter "compound_set_name" of String
        :returns: instance of type "compoundset_upload_results" -> structure:
           parameter "report_name" of String, parameter "report_ref" of
           String, parameter "compoundset_ref" of type "obj_ref"
        """
        return self._client.call_method(
            'CompoundSetUtils.compound_set_from_model',
            [params], self._service_ver, context)

    def export_compoundset_as_tsv(self, params, context=None):
        """
        :param params: instance of type "ExportParams" (input and output
           structure functions for standard downloaders) -> structure:
           parameter "input_ref" of String
        :returns: instance of type "ExportOutput" -> structure: parameter
           "shock_id" of String
        """
        return self._client.call_method(
            'CompoundSetUtils.export_compoundset_as_tsv',
            [params], self._service_ver, context)

    def export_compoundset_as_sdf(self, params, context=None):
        """
        :param params: instance of type "ExportParams" (input and output
           structure functions for standard downloaders) -> structure:
           parameter "input_ref" of String
        :returns: instance of type "ExportOutput" -> structure: parameter
           "shock_id" of String
        """
        return self._client.call_method(
            'CompoundSetUtils.export_compoundset_as_sdf',
            [params], self._service_ver, context)

    def status(self, context=None):
        return self._client.call_method('CompoundSetUtils.status',
                                        [], self._service_ver, context)
