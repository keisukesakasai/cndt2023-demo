/*instrumentation.js*/
// Require dependencies
const { NodeSDK } = require('@opentelemetry/sdk-node');
const { OTLPTraceExporter } = require("@opentelemetry/exporter-trace-otlp-grpc");
const { Resource, processDetector, hostDetector } = require('@opentelemetry/resources');
const { SemanticResourceAttributes } = require("@opentelemetry/semantic-conventions");

const {
    getNodeAutoInstrumentations,
} = require('@opentelemetry/auto-instrumentations-node');
const resource = Resource.default().merge(new Resource({
    [SemanticResourceAttributes.SERVICE_NAME]: "Node-App-With-Instrumented",
}));
const resourceDetectors = [processDetector, hostDetector];

const sdk = new NodeSDK({
    traceExporter: new OTLPTraceExporter({
        url: "http://localhost:4317",

    }),
    resource: resource,
    resourceDetectors: resourceDetectors,
    instrumentations: [
        getNodeAutoInstrumentations(
            {
                '@opentelemetry/instrumentation-fs': {
                    enabled: false,
                },
            })
    ],
});

sdk.start();