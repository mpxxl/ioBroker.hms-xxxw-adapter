#region Copyright notice and license
// Protocol Buffers - Google's data interchange format
// Copyright 2008 Google Inc.  All rights reserved.
//
// Use of this source code is governed by a BSD-style
// license that can be found in the LICENSE file or at
// https://developers.google.com/open-source/licenses/bsd
#endregion

using Google.Protobuf.Reflection;
using NUnit.Framework;
using System;
using System.Linq;

namespace Google.Protobuf.Test.Reflection;

public class FeatureSetDescriptorTest
{
    // Canonical serialized form of the edition defaults, generated by embed_edition_defaults.
    // TODO: Update this automatically.
    private const string DefaultsBase64 = "CrEBEqsBCAEQAhgCIAMoATAC6vAEMQj+//////////8BEAEYASABKAEwATgBQAFIAVABWABlzcyMP2oAcAB4AYIBBDIwMjPy8AQxCP7//////////wEQARgBIAEoATABOAFAAUgBUAFYAGXNzIw/agBwAHgBggEEMjAyM/rwBDEI/v//////////ARABGAEgASgBMAE4AUABSAFQAVgAZc3MjD9qAHAAeAGCAQQyMDIzGOYHCrEBEqsBCAIQARgBIAIoATAB6vAEMQj9//////////8BEAEYASABKAEwATgBQAFIAVABWABlzcyMP2oAcAB4AYIBBDIwMjPy8AQxCP3//////////wEQARgBIAEoATABOAFAAUgBUAFYAGXNzIw/agBwAHgBggEEMjAyM/rwBDEI/f//////////ARABGAEgASgBMAE4AUABSAFQAVgAZc3MjD9qAHAAeAGCAQQyMDIzGOcHCsMBEr0BCAEQARgBIAIoATAB6vAENwgBEAEYASABKAEwATgBQAFIAVABWABlzcyMP2oPCAEQAR0AAMA/IgQyMDIzcAF4AYIBBDIwMjPy8AQ3CAEQARgBIAEoATABOAFAAUgBUAFYAGXNzIw/ag8IARABHQAAwD8iBDIwMjNwAXgBggEEMjAyM/rwBDcIARABGAEgASgBMAE4AUABSAFQAVgAZc3MjD9qDwgBEAEdAADAPyIEMjAyM3ABeAGCAQQyMDIzGOgHIOgHKOgH";

    [Test]
    [TestCase(Edition.Proto2)]
    [TestCase(Edition.Proto3)]
    [TestCase(Edition._2023)]
    public void DefaultsMatchCanonicalSerializedForm(Edition edition)
    {
        var canonicalDefaults = FeatureSetDefaults.Parser
          .WithDiscardUnknownFields(true) // Discard language-specific extensions.
          .ParseFrom(Convert.FromBase64String(DefaultsBase64));
        var canonicalEditionDefaults = canonicalDefaults.Defaults.Single(def => def.Edition == edition).Features;
        var candidateEditionDefaults = FeatureSetDescriptor.GetEditionDefaults(edition).Proto;

        Assert.AreEqual(canonicalEditionDefaults, candidateEditionDefaults);
    }
}
