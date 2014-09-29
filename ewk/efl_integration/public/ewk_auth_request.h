/*
 * Copyright (C) 2012 Intel Corporation. All rights reserved.
 * Copyright (C) 2014 Samsung Electronics.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions
 * are met:
 * 1. Redistributions of source code must retain the above copyright
 *    notice, this list of conditions and the following disclaimer.
 * 2. Redistributions in binary form must reproduce the above copyright
 *    notice, this list of conditions and the following disclaimer in the
 *    documentation and/or other materials provided with the distribution.
 *
 * THIS SOFTWARE IS PROVIDED BY APPLE INC. AND ITS CONTRIBUTORS ``AS IS''
 * AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
 * THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
 * PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL APPLE INC. OR ITS CONTRIBUTORS
 * BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
 * CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
 * SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
 * INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
 * CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
 * ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF
 * THE POSSIBILITY OF SUCH DAMAGE.
 */

/**
 * @file    ewk_auth_request.h
 * @brief   Describes the Ewk Authentication Request API.
 */

#ifndef ewk_auth_request_h
#define ewk_auth_request_h

#include <Eina.h>

#ifdef __cplusplus
extern "C" {
#endif

/** Creates a type name for _Ewk_Auth_Challenge */
typedef struct _Ewk_Auth_Challenge Ewk_Auth_Request;

/**
 * Set credential for the authentication request.
 *
 * @param request request object to update
 *
 * @return @c EINA_TRUE if the credential was successfuly sent, @c EINA_FALSE otherwise.
 */
EAPI Eina_Bool ewk_auth_request_authenticate(Ewk_Auth_Request *request, const char *username, const char *password);

/**
 * Cancels the authentication request.
 *
 * @param request request object to cancel
 *
 * @return @c EINA_TRUE if successful, @c EINA_FALSE otherwise
 */
EAPI Eina_Bool ewk_auth_request_cancel(Ewk_Auth_Request *request);

/**
 * Queries the authentication realm.
 *
 * @param request request object to query
 *
 * @return the realm pointer, that may be @c NULL. This pointer is
 *         guaranteed to be eina_stringshare, so whenever possible
 *         save yourself some cpu cycles and use
 *         eina_stringshare_ref() instead of eina_stringshare_add() or
 *         strdup()
 */
EAPI const char *ewk_auth_request_realm_get(const Ewk_Auth_Request *request);

#ifdef __cplusplus
}
#endif

#endif /* ewk_auth_request_h */